import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MUCNonickComponent } from './muc-nonick/muc-nonick.component';
import { MucNickComponent } from './muc-nick/muc-nick.component';

@NgModule({
  declarations: [
    AppComponent,
    MUCNonickComponent,
    MucNickComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
