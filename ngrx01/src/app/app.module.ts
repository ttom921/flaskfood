import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { Testngrx01Component } from './testngrx01/testngrx01.component';
import { Testngrx02Component } from './testngrx02/testngrx02.component';
import { Testngrx03Component } from './testngrx03/testngrx03.component';
import { Testngrx04Component } from './testngrx04/testngrx04.component';

@NgModule({
  declarations: [
    AppComponent,
    Testngrx01Component,
    Testngrx02Component,
    Testngrx03Component,
    Testngrx04Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
