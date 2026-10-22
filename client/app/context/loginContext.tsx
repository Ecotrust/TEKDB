import React, {
  useEffect,
  createContext,
  useContext,
  useCallback,
} from "react";
import { submitAction } from "./action";
import { getAuthSession } from "../api/tekdbApi";

type UseLoginFormReturn = {
  isAuthenticated: boolean;
  isCheckingAuth: boolean;
  formAction: (formData: FormData) => void;
  isPending: boolean;
  error: string | null;
};

type useLogin = {
  loginForm: UseLoginFormReturn;
  showLoginModal: boolean;
  setShowLoginModal: React.Dispatch<React.SetStateAction<boolean>>;
};

const LoginContext = createContext<useLogin | null>(null);

export const LoginProvider: React.FC<React.PropsWithChildren<{}>> = ({
  children,
}) => {
  const [showLoginModal, setShowLoginModal] = React.useState(false);
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);
  const [isCheckingAuth, setIsCheckingAuth] = React.useState(true);
  const [isPending, setIsPending] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);

  useEffect(() => {
    let isMounted = true;

    const bootstrapAuth = async () => {
      try {
        const session = await getAuthSession();
        if (isMounted) {
          setIsAuthenticated(session.authenticated);
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
      const loginState = await submitAction(
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
    isAuthenticated,
    isCheckingAuth,
    formAction,
    isPending,
    error,
  };

  const value = {
    loginForm,
    showLoginModal,
    setShowLoginModal,
  };

  return (
    <LoginContext.Provider value={value}>{children}</LoginContext.Provider>
  );
};

export const useLogin = () => {
  const context = useContext(LoginContext);
  if (!context) {
    throw new Error("useLogin must be used within a LoginProvider");
  }
  return context as useLogin;
};
