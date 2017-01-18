import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home';
import { NoContent } from './components/no-content';

import { DataResolver } from './app.resolver';


export const ROUTES: Routes = [
  { path: '',      component: HomeComponent },
  { path: 'home',  component: HomeComponent },
  { path: '**',    component: NoContent },
];
