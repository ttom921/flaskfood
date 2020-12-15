import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { MessageBox } from 'src/app/_dialog/message-box';
import { MessageBoxButton, MessageBoxStyle } from 'src/app/_dialog/message-enums';
import { AuthenticationService } from 'src/app/_service/auth/authentication.service';
import { isNullOrUndefined } from 'src/app/_util/custutil';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  @Output() toggle = new EventEmitter<void>();
  isLoggedIn$: Observable<boolean>;
  login_name: string;
  constructor(
    private dialog: MatDialog,
    private router: Router,
    private authenticationService: AuthenticationService
  ) {
    this.isLoggedIn$ = this.authenticationService.isLoggedIn();
  }

  ngOnInit(): void {
    if (environment.debug != true) {
      if (!isNullOrUndefined(this.authenticationService.currentUserValue)) {
        this.login_name = this.authenticationService.currentUserValue.login_name;
      }
    }
  }
  onClick() {
    this.toggle.emit();
  }
  logout() {
    //console.log("logout");
    let message = "Are you sure logout?";
    let title = "";
    let information = "";
    let button = MessageBoxButton.YesNo;
    let allow_outside_click = false;
    let style = MessageBoxStyle.Simple;
    let width = "450px";
    MessageBox.show(this.dialog, message, title, information, button, allow_outside_click, style, width).subscribe(res => {
      //console.log(res);
      if (res.result == "yes") {
        this.authenticationService.logout();
        this.router.navigate(['/login']);
      }
      // let respone = "respones value=" + res;
      // MessageBox.show(this.dialog, `The result is : ${respone}`);
    });
  }

}
