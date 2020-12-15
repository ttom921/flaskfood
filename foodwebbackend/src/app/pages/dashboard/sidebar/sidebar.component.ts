import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Observable } from 'rxjs';
import { isNullOrUndefined } from 'src/app/_util/custutil';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
  isLoggedIn$: Observable<boolean>;
  @Output() navClicked = new EventEmitter<void>();
  constructor() { }

  ngOnInit(): void {
  }
  handleClicked(ev: Event) {
    if (!isNullOrUndefined(ev))
      ev.preventDefault();
    this.navClicked.emit();
  }
}
