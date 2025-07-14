export type UserRole = "député" | "président" | "rapporteur" ;
export type UserSexe = "homme" | "femme";
export type Direction = "Bureau" |"bureau_etudes";
export type UserCirconscription = "Funa" | "Mont Amba" | "Lukunga" | "Tshangu" | string;
export type UserPostePartie = "président" | "secrétaire" | "membre" | string;

export interface User {
  id: string;
  nom: string;
  postnom: string;
  prenom: string;
  email: string;
  sexe: UserSexe;
  circonscription: UserCirconscription;
  role: UserRole;
  partie_politique: string;
  poste_partie: UserPostePartie;
  direction: string;
  groupe_parlementaire: string;
  statut: boolean;
}

export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterData {
  email: string;
  password: string;
  nom: string;
  postnom: string;
  prenom: string;
  sexe: UserSexe;
  circonscription: UserCirconscription;
  role: UserRole;
  partie_politique: string;
  poste_partie: UserPostePartie;
  direction: string;
  groupe_parlementaire: string;
  statut: boolean;
}

