import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";

import { AuthService } from "../services/auth.service";

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.css"],
})
export class LoginComponent implements OnInit {
  usuario = {
    nom: "",
    pwd: "",
  };
  constructor(private authservice: AuthService, private router: Router) {}

  ngOnInit(): void {}
  inicio() {
    event.preventDefault();
    this.authservice.inicio(this.usuario).subscribe(
      (respuesta) => {
        if (respuesta[0].Id !== undefined) {
          localStorage.setItem("Id", respuesta[0].Id);
          localStorage.setItem("Rol", respuesta[0].Rol);
          this.router.navigate(["/principal"]);
        } else alert("usuario no existe");
      },
      (error) => {
        alert("Error, Intente mas tarde.");
      }
    );
  }
  exist() {
    if (localStorage.getItem("Id")) {
      this.router.navigate(["/principal"]);
      return true;
    } else return false;
  }
}
