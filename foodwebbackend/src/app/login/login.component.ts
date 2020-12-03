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
    "login_name": "",
    "login_pwd": "",
    "formError": ""
  };
  vaildationMessages = {
    "login_name": {
      "required": "郵箱必須輸入",
      "minlength": "請輸入至少要4位"
    },
    "login_pwd": {
      "required": "密碼必須輸入",
      "minlength": "密碼至少要4位"
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
      "login_name": [
        this.userInfo.login_name,
        [
          Validators.required,
          Validators.minLength(4),
        ]
      ],
      "login_pwd": [
        this.userInfo.login_pwd,
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
