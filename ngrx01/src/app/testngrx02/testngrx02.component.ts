import { Component, OnInit } from '@angular/core';
import { Subject, BehaviorSubject } from 'rxjs';
import { dispatch } from 'rxjs/internal/observable/pairs';
import { tap } from 'rxjs/operators';

interface Action {
  type: string,
  payload?: any
}
//dispatcher
class Dispatcher extends Subject<Action>{
  dispatch(act: Action) {
    console.log("got dispatch action ", act.type);
    this.next(act);
  }
}

class Store extends BehaviorSubject<Action>{
  constructor(private dispatcher: Dispatcher, initialState: Action) {
    super(initialState);
    this.dispatcher.pipe(
      tap(v => { console.log("do some effect for ", v.type) }),
      tap(v => { console.log("do some reducer here ,get new state after", v) }),
    ).subscribe(state => {
      //new state, push to subscriber
      super.next({ type: 'new state after ' + state.type });
    });
  }
  dispatch(act: Action) {
    this.dispatcher.dispatch(act);
  }
  //override next to allow store subscriber action$
  next(act: Action) {
    this.dispatcher.dispatch(act);
  }
}
@Component({
  selector: 'app-testngrx02',
  templateUrl: './testngrx02.component.html',
  styleUrls: ['./testngrx02.component.scss']
})
export class Testngrx02Component implements OnInit {

  constructor() { }

  ngOnInit(): void {
    this.testngrxdisstore()
  }
  testngrxdisstore() {
    // instanciate new store
    const dispatcher = new Dispatcher();
    const store = new Store(dispatcher, { type: 'initial State' });

    //add subscriber
    const sub1 = store.subscribe(v => console.log('sub1 ===> ', v));

    // start dispatch action
    store.dispatch({ type: 'Action1' });//dispatch new action to store
    store.dispatch({ type: 'Action2' });//// dispatch another action
  }

}
