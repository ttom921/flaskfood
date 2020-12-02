import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from '../_service/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  //#region form 相關
  formModel: FormGroup;
  hide = true;
  userInfo: any = {};
  formErrors = {
    "email": "",
    "password": "",
    "formError": ""
  };
  vaildationMessages = {
    "email": {
      "required": "郵箱必須輸入",
      "email": "請輸入正確的郵箱地址"
    },
    "password": {
      "required": "密碼必須輸入",
      "minlength": "密碼至少要5位"
    }
  };
  //#endregion form 相關
  constructor(
    private fb: FormBuilder,
    private router: Router,
    private userService: UserService
  ) { }

  ngOnInit(): void {
    this.buildForm();
  }
  buildForm() {
    this.formModel = this.fb.group({
      "email": [
        this.userInfo.email,
        [
          Validators.required,
          Validators.email,
        ]
      ],
      "password": [
        this.userInfo.password,
        [
          Validators.required,
          Validators.minLength(4),
        ]
      ]
    });
    this.formModel.valueChanges.subscribe(data => {
      this.onValueChange(data);
    });
  }
  onValueChange(data?: any) {
    if (!this.formModel) {
      return;
    }
    //檢查是否有錯誤和顯示錯誤訊息
    const form = this.formModel;
    for (const field in this.formErrors) {
      this.formErrors[field] = "";
      const control = form.get(field);
      if (control && control.dirty && !control.valid) {
        const messages = this.vaildationMessages[field];
        for (const key in control.errors) {
          this.formErrors[field] += messages[key] + " ";
        }
      }
    }
  }
  onSubmit(e) {
    if (this.formModel.valid) {
      console.log(this.formModel.value);
      this.userService.Post(this.formModel.value).subscribe(res => {
        console.log(res);
      });
    }
  }
}
