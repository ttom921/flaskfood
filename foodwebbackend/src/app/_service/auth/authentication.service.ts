import { UserInfo } from './../../_models/user-info';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor() { }
  loginSuccess(username: string, password: string, resdata: any) {
    //console.log(resdata);
    let user = new UserInfo;
    user.login_name = username;
    user.user_token = resdata.data.authtoken;
    //console.log(user);
    localStorage.setItem('foodUser', JSON.stringify(user));

  }
}
