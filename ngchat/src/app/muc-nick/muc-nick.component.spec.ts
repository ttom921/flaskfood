import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MucNickComponent } from './muc-nick.component';

describe('MucNickComponent', () => {
  let component: MucNickComponent;
  let fixture: ComponentFixture<MucNickComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MucNickComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MucNickComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
