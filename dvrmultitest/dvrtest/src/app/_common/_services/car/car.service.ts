import { HttpBackend, HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { TokenService } from '../token.service';

@Injectable({
  providedIn: 'root'
})
export class CarService {
  api = `${environment.apiUrl}/cars`;

  private httpClient: HttpClient;

  constructor(
    private tokenService: TokenService,
    private http: HttpClient,
    handler: HttpBackend) {
    // 不使用httpinterceptor
    this.httpClient = new HttpClient(handler);
  }
  //gps
  Put(data) {
    return this.http.put<any>(this.api, data, this.getHttpHead());
  }
  private getHttpHead(): { headers: HttpHeaders } {
    // const headers = new HttpHeaders().set(InterceptorSkipHeader, '');
    // console.log(data);
    let carinfo = this.tokenService.currentCarValue;
    const httpOptions = {
      headers: new HttpHeaders({
        Authorization: `${carinfo.car_token}`,
        Waiting: "True"
      }),
    };

    return httpOptions;
  }
}
