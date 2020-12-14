import { UserInfo } from './../../_models/user-info';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  private currentUserSubject$: BehaviorSubject<UserInfo>;
  constructor() {
    this.currentUserSubject$ = new BehaviorSubject<UserInfo>(
      JSON.parse(localStorage.getItem('foodUser'))
    );
    console.log(
      `environment api=${environment.apiUrl} production=${environment.production}`
    );
  }
  /**
   * 取得使用者資訊
   * @readonly
   * @type {UsersInfo}
   * @memberof AuthenticationService
   */
  get currentUserValue(): UserInfo {
    return this.currentUserSubject$.value;
  }
  loginSuccess(username: string, password: string, resdata: any) {
    //console.log(resdata);
    let user = new UserInfo;
    user.login_name = username;
    user.user_token = resdata.data.authtoken;
    //console.log(user);
    localStorage.setItem('foodUser', JSON.stringify(user));

  }
}
