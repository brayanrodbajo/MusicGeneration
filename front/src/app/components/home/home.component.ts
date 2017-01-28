import { Component } from '@angular/core';
import { Http, Response } from '@angular/http';
import { APIService } from '../../services';

@Component({
  selector: 'home',
  providers: [
    APIService
  ],
  templateUrl: './home.template.html',
  styleUrls: ['./home.style.less']
})
export class HomeComponent {
    private showPlayer : boolean;
    private tonality : string;
    private tempo : string;
    private inCommunication : boolean;
    private track: string;
    private components: string;

    constructor(private http: Http, private api: APIService) {
        this.showPlayer = false;
        this.inCommunication = false;
    }

    /**
    * Fetch the data from the python-flask backend
    */
    public generate() {
        this.inCommunication = true;
        this.showPlayer = false;
        this.api.generate(this.tonality, this.tempo)
        .subscribe(
            resp => {
                this.inCommunication = false;
                this.showPlayer  = true;
		this.components = resp.components;
                console.log(resp);
                // const mediaType = 'audio/wav';
                // const blob = new Blob([resp._body], {type: mediaType});
                // const filename = 'combined.wav';
                // FileSaver.saveAs(blob, filename);
                // const fileURL = window.URL.createObjectURL(file);
                // a.href = fileURL;
                // a.download = fileName;
                // a.click();
            },
            err => {
                this.inCommunication = false;
                console.log('error in generate ' + err);
                throw (err);
            }
        );
    }
}
