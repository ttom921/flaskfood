import { Component } from '@angular/core';
import { UserService } from './_service/user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'foodwebbackend';
  constructor(private userService: UserService) {
    this.userService.Gets().subscribe(res => {
      console.log(res);
    });
  }
}
