import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { map } from 'rxjs/operators';
import { WebsocketService } from 'src/app/_service/websocket.service';

//const CHAT_URL = 'ws://192.168.83.128:5000/v0.0/ws/echo';
//const CHAT_URL = 'ws://192.168.40.191:5000/v0.0/ws/echo';
//const CHAT_URL = 'ws://192.168.40.191:5000/websocket';
//const CHAT_URL = 'ws://192.168.40.191:5000/v0.0/ws/echo';
const CHAT_URL = 'ws://192.168.40.191/v0.6/websocket/echo';

export interface Message {
  author: string,
  message: string
}

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  public messages: Subject<Message>;
  constructor(websocketService: WebsocketService) {
    this.messages = <Subject<Message>>websocketService
      .connect(CHAT_URL)
      .pipe(map((response: MessageEvent): Message => {
        let data = JSON.parse(response.data);
        return {
          author: data.author,
          message: data.message
        }
      }));
  }
}
