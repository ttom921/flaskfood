import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MemberRoutingModule } from './member-routing.module';
import { SharedAngularMaterialModule } from '../share/shared-angular-material/shared-angular-material.module';


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    MemberRoutingModule,
    SharedAngularMaterialModule,
  ]
})
export class MemberModule { }
