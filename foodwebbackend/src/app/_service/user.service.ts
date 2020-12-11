import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  api = `${environment.apiUrl}/user/login`;
  constructor(private http: HttpClient) { }
  Gets() {
    return this.http.get<any>(this.api);
  }
  Post(data) {
    return this.http.post<any>(this.api, data);
  }
  example() {
    let url = `${environment.apiUrl}/user/example`;
    return this.http.get<any>(url);
  }
}
