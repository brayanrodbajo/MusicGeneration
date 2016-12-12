import { Component, OnInit } from '@angular/core';
import { Http, Response } from '@angular/http';
import { AuthenticationService } from '../authentication';
import { Router } from '@angular/router';
import { NavbarComponent } from  '../navbar';
import { APIService } from '../services';

@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [APIService]
})
export class HomeComponent {

  private showPlayer : boolean;
  private path : string;
  private tonality : string;
  private tempo : string;

  constructor(private http: Http, private router: Router,
    private api: APIService) {
    this.showPlayer = false;
  }

  /**
   * Fetch the data from the python-flask backend
   */
  public generate() {
    this.api.generate(this.tonality, this.tempo)
      .subscribe( path => {
        this.showPlayer  = true;
        this.path = path;
      },
      err => throw (err)
      );
  }
}
