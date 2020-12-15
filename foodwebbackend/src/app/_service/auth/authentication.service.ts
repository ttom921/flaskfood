import { UserInfo } from './../../_models/user-info';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  private currentUserSubject$: BehaviorSubject<UserInfo>;
  isLoginSubject$ = new BehaviorSubject<boolean>(this.hasToken());
  constructor() {
    this.currentUserSubject$ = new BehaviorSubject<UserInfo>(
      JSON.parse(localStorage.getItem('foodUser'))
    );
    console.log(`environment api=${environment.apiUrl} production=${environment.production}`);
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
  /**
  * 登入失敗
  * @param {*} errmsg
  * @memberof AuthenticationService
  */
  loginFail(errmsg) {
    this.currentUserSubject$.error(errmsg);
  }
  /**
   * 登入成功
   *
   * @param {string} username
   * @param {string} password
   * @param {*} data
   * @memberof AuthenticationService
   */
  loginSuccess(username: string, password: string, resdata: any) {
    //console.log(resdata);
    let user = new UserInfo;
    user.login_name = username;
    user.user_token = resdata.data.authtoken;
    //console.log(user);
    localStorage.setItem('foodUser', JSON.stringify(user));
    this.currentUserSubject$.next(user);

  }
  /**
   * 登出
   * @memberof AuthenticationService
   */
  logout() {

    // remove user from local storage to log user out
    localStorage.removeItem('foodUser');
    this.currentUserSubject$.next(null);
  }
  /**
   * 如果有取得token, 表示使用者有登入系統
   * @private
   * @returns {boolean}
   * @memberof AuthenticationService
   */
  private hasToken(): boolean {
    //let res = localStorage.getItem('currentUser');
    //console.log("hasToken->" + res);
    return !!localStorage.getItem("currentUser");
  }
  isLoggedIn(): Observable<boolean> {
    return this.isLoginSubject$.asObservable();
  }
}
