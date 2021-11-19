import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Testngrx03Component } from './testngrx03.component';

describe('Testngrx03Component', () => {
  let component: Testngrx03Component;
  let fixture: ComponentFixture<Testngrx03Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Testngrx03Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Testngrx03Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
