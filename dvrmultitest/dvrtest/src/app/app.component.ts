import { Component, OnDestroy, OnInit } from '@angular/core';
import { TokenService } from './_common/_services/token.service';
import * as moment from 'moment';
// import * as SHA from 'sha.js';
// const shajs = require('sha.js')
import * as sha1 from 'js-sha1';
import { CarService } from './_common/_services/car/car.service';
// declare model
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'dvrtest';
  caruid = "";
  caruid_list = [
    "6e:b3:d2:b9:1f:93",
    //  "6e:b3:d2:b9:1f:93"
  ];
  // caruid_list = [
  //   //"00:0f:3a:03:10:f4",
  //   //"00:0f:3a:03:10:eb",
  //   //"00:0f:3a:03:11:dd",
  //   //"00:0f:3a:03:10:f3",
  //   //"00:0f:3a:03:68:21"
  // ];


  polling: any = null;
  updatetime = 3;
  isClicked = false;
  constructor(
    private tokenService: TokenService,
    private carService: CarService
  ) {
    localStorage.removeItem('currentCar');

  }

  ngOnInit(): void {
    //
    // 6 -> 10
    let rndint = Math.floor(Math.random() * 4) + 6;
    this.updatetime = rndint;
    console.log(`setInterval ${this.updatetime}`);
    //
    this.login();
  }
  ngOnDestroy(): void {
    //console.log(`FwStatusList->ngOnDestroy`);
    if (this.polling) {
      clearInterval(this.polling);
    }
  }
  login() {
    localStorage.removeItem('currentCar');
    //sha1('Message to hash');
    var hash = sha1.create();
    hash.update('Message to hash').hex();
    //hash.hex();
    //sha1("_" + vendor_id + dvr_uid + utc + "_") # sha1 中的dvr_uid將":" 用"#"替代
    //let hash = sha1('sha256').update('Abc123$').digest('hex');
    //console.log(`hash=${hash}`);
    let todaytime = moment(new Date()).format("YYYY-MM-DD");
    //console.log(`today=${todaytime}`);
    let utctime = Math.round(moment(`${todaytime} 00:00:00Z`, 'YYYY-MM-DD hh:mm:ssZ').utc().valueOf() / 1000);

    //let utctime = Math.round(moment.utc().valueOf() / 1000);
    console.log(`utctime=${utctime}`);
    this.caruid = this.getrnddvr();// this.caruid_list[0];

    let senddata = {
      "dvr_uid": this.caruid,
      "vendor_id": "ViewTec",
      "utc": utctime,
      "token": hash
    };
    senddata.token = this.getsha1(senddata);
    console.log(`senddata=`, senddata);

    this.tokenService.login(senddata).subscribe(
      res => {
        console.log(res);
        this.tokenService.loginSuccess(
          res.car_id,
          res
        );
      },
      (error) => {
        console.error(error);
      }
    );
  }
  getsha1(data) {
    //sha1("_" + vendor_id + dvr_uid + utc + "_") # sha1 中的dvr_uid將":" 用"#"替代
    let caruidstr = data.dvr_uid.replaceAll(':', '#');
    //console.log(`getsha1->${caruidstr}`);
    let crpmsg = `_${data.vendor_id}${caruidstr}${data.utc}_`;
    console.log(`crpmsg->*******${crpmsg}*******`);
    let hash = sha1.create();
    hash.update(`${crpmsg}`).hex();
    console.log(`hex->******${hash}******`);
    return `${hash}`
  }
  getrnddvr() {
    let lstleng = this.caruid_list.length;
    // 0 -> n
    let rndint = Math.floor(Math.random() * lstleng);
    return this.caruid_list[rndint];

  }
  sendgps() {
    // let utctime = moment.utc().valueOf();
    // let dvrutctime = Math.round(utctime / 1000);
    let utctime = Math.round(moment.utc().valueOf() / 1000);
    let dvrutctime = utctime;
    let senddata = {
      "dvrUTCTime": dvrutctime,
      "dvrIP": "192.168.0.1",
      "dvrGateway": "192.168.0.254",
      "dvrNetMode": "WWAN",
      "ign": true,
      "heading": 11111,
      "gps": [
        {
          "time": utctime,//123456790.111,
          "latitude": 123.5,
          "longitude": 123.5,
          "altitude": 123.5,
          "satNum": 5,
          "fix": true,
          "heading": 12,
          "speed": 80.5
        },
        {
          "time": utctime,//123456789.123,
          "speed": 80.5
        }
      ],
      "gsensor": [
        {
          "time": utctime,//123456790.111,
          "x": 123.55,
          "y": 123.55,
          "z": 123.55
        },
        {
          "time": utctime,//123456789.222,
          "x": 123.55,
          "y": 123.55,
          "z": 123.55
        }
      ]
    };
    this.carService.Put(senddata).subscribe(
      res => {
        console.log(`send time->${utctime}`);
      },
      (error) => {
        console.error(error);
      }
    );
  }
  startsend() {
    this.isClicked = true;
    this.polling = setInterval(() => {
      //console.log(`setInterval`);
      this.sendgps();
    }, this.updatetime * 1000);
  }
}
