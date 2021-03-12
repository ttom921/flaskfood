# Webkafka

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 10.2.0.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.

## 加入AngularMateial

```
ng add @angular/material
```

目前選擇`indigo-pink `

加入theme設定
在’styles.scss’中,有四種選一種

```scss
//@import "~@angular/material/prebuilt-themes/deeppurple-amber.css";
//@import "~@angular/material/prebuilt-themes/indigo-pink.css";
//@import "~@angular/material/prebuilt-themes/pink-bluegrey.css";
//@import "~@angular/material/prebuilt-themes/purple-green.css";
```

加入SharedAngularMaterial <https://ithelp.ithome.com.tw/articles/10209937>

```
ng g m share\SharedAngularMaterial
```

在MatIcon中使用SVG

必須透過Angular提供的DomSanitizer Service來信任這個路徑。接著我們就可以透過MatIconRegistry來擴充SVG icon

```typescript
export class SharedAngularMaterialModule implements OnInit {
  constructor(private matIconRegistry: MatIconRegistry, private domSanitizer: DomSanitizer) {
    this.ngOnInit();
  }
  ngOnInit(): void {
    // this.matIconRegistry.addSvgIconInNamespace(
    //   "custom-svg",
    //   "angular",
    //   this.domSanitizer.bypassSecurityTrustResourceUrl("assets/images/angular_solidBlack.svg")
    // );
  }
```

## 在MatIcon中使用Icon Font

```bash
npm install --save @fortawesome/fontawesome-free
```

接下來在src\styles.scss中

```scss
//@import "~@angular/material/prebuilt-themes/deeppurple-amber.css";
//@import "~@angular/material/prebuilt-themes/indigo-pink.css";
//@import "~@angular/material/prebuilt-themes/pink-bluegrey.css";
//@import "~@angular/material/prebuilt-themes/purple-green.css";
@import "~@fortawesome/fontawesome-free/css/all.css";
```

## 加入normalize.css

```
npm install normalize.css
```



## 加入flexlayout

```
npm install --save @angular/flex-layout@10.0.0-beta.32
```

## 修改environment.ts和environment.prod.ts

````typescript
export const environment = {
   production: false,
  debug: false,
  //apiUrl: 'http://172.18.2.150/allen'
  // apiUrl: 'http://172.18.2.160/allen'
  //apiUrl: 'http://172.18.2.160/ttom'
  //apiUrl: 'http://172.18.2.160/v0.4'
  //apiUrl: 'http://172.18.2.160/v0.4'
  //apiUrl: '/v0.5'
  apiUrl: '/v0.0'
  //apiUrl: 'http://64.141.182.94/v0.4'
};

````

## CORS問題

在Edge下目它有bug，所以使用外掛來處理

可以在專案的根目錄下加入`proxy.config.json`檔案，內容如下

```json
{
  "/v0.0/*": {
    "target": "http://192.168.40.209",
    "secure": false,
    "logLevel": "debug"
  }
}
```

修改`package.json`

````json
"scripts": {
    "ng": "ng",
    "start": "ng serve --port=4200 --host=0.0.0.0 --disable-host-check --proxy-config proxy.config.json",
    "build": "ng build",
    "test": "ng test",
    "lint": "ng lint",
    "e2e": "ng e2e"
  },
````

先來建立資料夾`src\app\_helpers`再建立`httpconfig.interceptor.ts`