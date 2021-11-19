import { dispatch } from 'rxjs/internal/observable/pairs';
import { Subject, BehaviorSubject } from 'rxjs';
import { Component, OnInit } from '@angular/core';
import { scan, tap } from 'rxjs/operators';

interface Action {
  type: string;
  payload?: any
}
class Dispatcher extends Subject<Action>{
  dispatch(act: Action) {
    //console.log("get dispatch ", act.type);
    this.next(act);
  }
}

class Store extends BehaviorSubject<Action>{
  constructor(private dispatcher: Dispatcher, private reducer: any, initialState: any) {
    super(initialState);
    this.dispatcher.pipe(
      tap(v => { console.log("do som effect for ", v.type) }),
      scan((s, v) => this.reducer(s, v), initialState)
    )
      .subscribe(state => {
        super.next(state);// new state , push to subscriber
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
//reducer
const message = (state = [], action: Action) => {
  switch (action.type) {
    case 'ADD_MESSAGE':
      return [...state, action.payload];
    case 'REMOVE_MESSAGE':
      return state.filter((msg: any) => msg.id != action.payload);
    default:
      return state;
  }
}
@Component({
  selector: 'app-testngrx03',
  templateUrl: './testngrx03.component.html',
  styleUrls: ['./testngrx03.component.scss']
})
export class Testngrx03Component implements OnInit {

  constructor() { }

  ngOnInit(): void {
    this.testngrx01();
  }
  testngrx01() {
    // instanciate new store
    const initialState: any = [];
    const dispatcher = new Dispatcher();
    const store = new Store(dispatcher, message, initialState);

    //add suscriber
    const sub1 = store.subscribe(v => console.log("message ==> ", v));

    // start dispatch action
    store.dispatch({ type: 'ADD_MESSAGE', payload: { id: 1, message: "First message" } });
    store.dispatch({ type: 'ADD_MESSAGE', payload: { id: 2, message: "second message" } });
    store.dispatch({ type: 'REMOVE_MESSAGE', payload: 2 });
    store.dispatch({ type: 'ADD_MESSAGE', payload: { id: 3, message: "Third message" } });
  }

}
