import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UserRoutingModule } from './user-routing.module';
import { LoginComponent } from './login/login.component';
import { SharedAngularMaterialModule } from '../share/shared-angular-material/shared-angular-material.module';


@NgModule({
  declarations: [
    LoginComponent
  ],
  imports: [
    CommonModule,
    UserRoutingModule,
    SharedAngularMaterialModule,
  ]
})
export class UserModule { }
