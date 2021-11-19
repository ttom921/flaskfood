import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Testngrx02Component } from './testngrx02.component';

describe('Testngrx02Component', () => {
  let component: Testngrx02Component;
  let fixture: ComponentFixture<Testngrx02Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Testngrx02Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Testngrx02Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
