import React, {
  useEffect,
  createContext,
  use,
  useCallback,
} from "react";
import type { ReactNode } from "react";
import { submitLoginAction } from "./action";
import { getAuthSession } from "../api/tekdbApi";

type UseLoginFormReturn = {
  isAuthenticated: boolean;
  isCheckingAuth: boolean;
  formAction: (formData: FormData) => void;
  isPending: boolean;
  error: string | null;
  username: string | null;
};

type useLogin = {
  loginForm: UseLoginFormReturn;
  showLoginModal: boolean;
  setShowLoginModal: React.Dispatch<React.SetStateAction<boolean>>;
};

const LoginContext = createContext<useLogin | null>(null);

interface LoginProviderProps {
  children: ReactNode;
}

export const LoginProvider: React.FC<LoginProviderProps> = ({
  children,
}) => {
  const [showLoginModal, setShowLoginModal] = React.useState(false);
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);
  const [isCheckingAuth, setIsCheckingAuth] = React.useState(true);
  const [isPending, setIsPending] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);
  const [username, setUsername] = React.useState<string | null>(null);

  useEffect(() => {
    let isMounted = true;

    const bootstrapAuth = async () => {
      try {
        const session = await getAuthSession();
        if (isMounted) {
          setIsAuthenticated(session.authenticated);
          setUsername(session.username ? session.username : null);
        }
      } catch (bootstrapError) {
        if (isMounted) {
          setIsAuthenticated(false);
        }
        console.error("Unable to load auth session", bootstrapError);
      } finally {
        if (isMounted) {
          setIsCheckingAuth(false);
        }
      }
    };

    bootstrapAuth();

    return () => {
      isMounted = false;
    };
  }, []);

  const formAction = useCallback(async (formData: FormData) => {
    setIsPending(true);
    try {
      const loginState = await submitLoginAction(
        {
          success: false,
          error: null,
        },
        formData
      );

      if (loginState.success) {
        setIsAuthenticated(true);
        setError(null);
        setShowLoginModal(false); 
        return;
      }

      setIsAuthenticated(false);
      setError(loginState.error || "Invalid username or password");
    } finally {
      setIsPending(false);
    }
  }, []);

  const loginForm = {
    formAction,
    isPending,
    error,
    isAuthenticated,
    isCheckingAuth,
    username,
  };

  const value = {
    loginForm,
    showLoginModal,
    setShowLoginModal,
  };

  return (
    <LoginContext value={value}>{children}</LoginContext>
  );
};

export const useLogin = () => {
  const context = use(LoginContext);
  if (!context) {
    throw new Error("useLogin must be used within a LoginProvider");
  }
  return context as useLogin;
};
