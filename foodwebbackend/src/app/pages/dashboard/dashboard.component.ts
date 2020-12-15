import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSidenavContent } from '@angular/material/sidenav';
import { UserService } from 'src/app/_service/user.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  @ViewChild('benji', { static: false }) el: MatSidenavContent;
  constructor(
    private userService: UserService,
  ) { }

  ngOnInit(): void {
    this.userService.example().subscribe(res => {
      console.log(res);
    });
  }
  onActivate(event) {
    //讓內容移到最上面
    if (this.el && this.el.getElementRef()) {
      this.el.getElementRef().nativeElement.scrollTop = 0;
    }
  }

}
