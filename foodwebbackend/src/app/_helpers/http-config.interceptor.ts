import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpResponse,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { AuthenticationService } from '../_service/auth/authentication.service';


@Injectable()
export class HttpConfigInterceptor implements HttpInterceptor {

  constructor(
    private authenticationService: AuthenticationService
  ) { }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    //有token
    // add authorization header with basic auth credentials if available
    const currentUser = this.authenticationService.currentUserValue;
    //console.log(`HttpConfigInterceptor currentUser=`, currentUser);
    if (currentUser) {
      const token: string = currentUser.user_token;
      //console.log(`HttpConfigInterceptor token=`, token);
      if (token) {
        request = request.clone({ headers: request.headers.set('Authorization', token) });
      }
    }
    // if (!request.headers.has('Content-Type')) {
    //   request = request.clone({ headers: request.headers.set('Content-Type', 'application/json') });
    // }

    //request = request.clone({ headers: request.headers.set('Accept', 'application/json') });

    return next.handle(request).pipe(
      map((event: HttpEvent<any>) => {
        if (event instanceof HttpResponse) {
          //console.log('event--->>>', event);
          // this.errorDialogService.openDialog(event);
        }
        return event;
      }),
      catchError((error: HttpErrorResponse) => {
        let data = {};
        data = {
          reason: error && error.error && error.error.reason ? error.error.reason : '',
          status: error.status
        };
        //this.errorDialogService.openDialog(data);
        return throwError(error);
      }));
  }
}
