import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SharedAngularMaterialModule } from './share/shared-angular-material/shared-angular-material.module';
import { LoginComponent } from './login/login.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { SimpleDialogComponent } from './_dialog/simple-dialog/simple-dialog.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    NotFoundComponent,
    SimpleDialogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    SharedAngularMaterialModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents: [SimpleDialogComponent],
})
export class AppModule { }
