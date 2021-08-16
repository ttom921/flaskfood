import { HttpBackend, HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { CarInfo } from '../_models/car-info';

@Injectable({
  providedIn: 'root'
})
export class TokenService {
  api = `${environment.apiUrl}/tokens/car`;
  private currentCarSubject$: BehaviorSubject<CarInfo>;
  private httpClient: HttpClient;
  constructor(private http: HttpClient, handler: HttpBackend) {
    this.currentCarSubject$ = new BehaviorSubject<CarInfo>(
      JSON.parse(localStorage.getItem('currentCar'))
    );
    // 不使用httpinterceptor
    this.httpClient = new HttpClient(handler);
  }

  get currentCarValue() {
    return this.currentCarSubject$.value;
  }
  login(data): Observable<any> {
    // console.log(data);
    return this.httpClient.post<any>(this.api, data, this.getHttpHead(data));
  }
  loginSuccess(car_id, data: any): void {
    // //console.log(jQuery.parseJSON(data).token);
    // //console.log(jQuery.parseJSON(data).user_role_id);
    // //let token = jQuery.parseJSON(data).token;
    // let user = new UsersInfo();
    // user.user_id = username;
    // user.user_password = "*******";
    // user.user_token = token;
    // user.user_role_id = jQuery.parseJSON(data).user_role_id;
    // localStorage.setItem('currentUser', JSON.stringify(user));
    // this.currentUserSubject$.next(user);
    // console.log(`loginSuccess data=`, data);
    const token = data.token;
    const user_role_id = data.user_role_id;
    const car = new CarInfo();
    car.car_id = car_id
    car.car_token = token;
    localStorage.setItem('currentCar', JSON.stringify(car));
    this.currentCarSubject$.next(car);
  }
  private hasToken(): boolean {
    // let res = localStorage.getItem('currentUser');
    // console.log("hasToken->" + res);
    return !!localStorage.getItem('currentCar');
  }
  private getHttpHead(data): { headers: HttpHeaders } {
    // const headers = new HttpHeaders().set(InterceptorSkipHeader, '');
    // console.log(data);
    const httpOptions = {
      headers: new HttpHeaders({
        Authorization: `${data.token}`,
      }),
    };

    return httpOptions;
  }
}
