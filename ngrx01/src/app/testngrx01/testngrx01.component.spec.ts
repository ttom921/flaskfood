import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Testngrx01Component } from './testngrx01.component';

describe('Testngrx01Component', () => {
  let component: Testngrx01Component;
  let fixture: ComponentFixture<Testngrx01Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Testngrx01Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Testngrx01Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
