import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MUCNonickComponent } from './muc-nonick.component';

describe('MUCNonickComponent', () => {
  let component: MUCNonickComponent;
  let fixture: ComponentFixture<MUCNonickComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MUCNonickComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MUCNonickComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
