import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Rx';
import { Http, Headers, Response, RequestOptions } from '@angular/http';
import {   Router } from '@angular/router';
import { jsonHeader } from '../utils';

@Injectable()
export class APIService {

  private loginSuccessful: boolean = true;


  constructor(private http: Http,
    private router: Router) {

  }

  /**
   * Sends a login request
   *
   */
  public generate(tonality: string, tempo: string) {
      let params: URLSearchParams = new URLSearchParams();
      params.set('tonality', tonality);
      params.set('tempo', tempo);

      let url = this.apiBaseUrl + '/generate';

      return this.request({'url': url, 'params': params});
  }
    /*
    To make the request to the API in the same format for all of them
     */
  private request( call ) {
      let url = call.url;
      let method = call.method || RequestMethod.Get;
      let params = call.params;
      let body = call.body || '';

      return this.http.request(new Request({
        method: method,
        url: url,
        search: params,
        body: body
      })).map(res => res.json());
    }
}
