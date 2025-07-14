import React, { createContext, useContext, useState, useEffect, ReactNode } from "react";
import api from "@/lib/api";
import { User, AuthState, LoginCredentials, RegisterData } from "@/types/auth";

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (credentials: LoginCredentials) => Promise<void>;
  logout: () => void;
  register: (data: RegisterData) => Promise<void>;
  updateUser: (updatedData: Partial<User>) => void; // Ajout updateUser
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [authState, setAuthState] = useState<AuthState>({
    user: null,
    isAuthenticated: false,
    isLoading: true,
  });

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const response = await api.get("token/refresh/");
        setAuthState({
          user: response.data.user,
          isAuthenticated: true,
          isLoading: false,
        });
      } catch (err) {
        setAuthState({
          user: null,
          isAuthenticated: false,
          isLoading: false,
        });
      }
    };
    checkAuth();
  }, []);

  const login = async (credentials: LoginCredentials) => {
    try {
      const response = await api.post("token/", credentials);
      setAuthState({
        user: response.data.user,
        isAuthenticated: true,
        isLoading: false,
      });
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);
    } catch (err) {
      throw new Error("Échec de la connexion");
    }
  };

  const logout = () => {
    setAuthState({
      user: null,
      isAuthenticated: false,
      isLoading: false,
    });
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
  };

  const register = async (data: RegisterData) => {
    try {
      const response = await api.post("register/", data);
      setAuthState({
        user: response.data.user,
        isAuthenticated: true,
        isLoading: false,
      });
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);
    } catch (err) {
      throw new Error("Échec de l'inscription");
    }
  };

  // Fonction pour mettre à jour localement les données utilisateur
  const updateUser = (updatedData: Partial<User>) => {
    setAuthState((prevState) => {
      if (!prevState.user) return prevState;
      return {
        ...prevState,
        user: {
          ...prevState.user,
          ...updatedData,
        },
      };
    });
  };

  return (
    <AuthContext.Provider
      value={{ ...authState, login, logout, register, updateUser }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
