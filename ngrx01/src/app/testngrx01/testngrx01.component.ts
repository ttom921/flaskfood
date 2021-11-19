import { Component, OnInit } from '@angular/core';
import { BehaviorSubject, Subject } from 'rxjs';

interface Action {
  type: string,
  payload?: any
}
//dispatcher
class Dispatcher extends Subject<Action>{
  dispatch(action: Action) {
    this.next(action);
  }
}
//
//first store with subject
class FirstStore extends Subject<Action> { }
// user BehaviorSubject
class SecondStore extends BehaviorSubject<Action>{
  constructor(initialState: Action) {
    super(initialState)
  }
}
@Component({
  selector: 'app-testngrx01',
  templateUrl: './testngrx01.component.html',
  styleUrls: ['./testngrx01.component.scss']
})


export class Testngrx01Component implements OnInit {

  constructor() { }

  ngOnInit(): void {
    //this.testngrxsample();
    //this.testFirstStore();
    this.testSecondStore();

  }
  testSecondStore() {
    const secondStore = new SecondStore({ type: 'initial State' });
    const sub4 = secondStore.subscribe(v => console.log("secondStore sub4 ===> ", v));
    const sub5 = secondStore.subscribe(v => console.log("secondStore sub5 ===> ", v));
    secondStore.next({ type: 'Action2' });
    const sub6 = secondStore.subscribe(v => console.log("secondStore sub6 ===> ", v));
    // sub6 get state as well
  }
  testFirstStore() {
    const firstStore = new FirstStore();
    const sub1 = firstStore.subscribe(v => console.log("firststore sub1 ===> ", v));
    const sub2 = firstStore.subscribe(v => console.log("firststore sub2 ===> ", v));
    firstStore.next({ type: 'Action1' });
    const sub3 = firstStore.subscribe(v => console.log("firststore sub3 ===> ", v));
    //sub3 did not get current state
  }
  testngrxsample() {
    const dispatcher = new Dispatcher();

    const suscribe1 = dispatcher.subscribe(v => console.log('sub1===>', v));
    const suscribe2 = dispatcher.subscribe(v => console.log('sub2===>', v));

    dispatcher.dispatch({ type: 'Action1' });
    dispatcher.dispatch({ type: 'Action2' });
  }

}
