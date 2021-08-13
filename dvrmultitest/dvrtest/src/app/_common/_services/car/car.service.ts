import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CarService {
  api = `${environment.apiUrl}/cars`;
  constructor(private http: HttpClient) { }
  //gps
  Put(data) {
    return this.http.put<any>(this.api, data);
  }
}
