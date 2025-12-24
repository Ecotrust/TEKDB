import React, {
  useActionState,
  useEffect,
  createContext,
  useContext,
} from "react";
import { LoginState, submitAction } from "./action";

type UseLoginFormReturn = {
  isAuthenticated: boolean;
  formAction: (formData: FormData) => void;
  isPending: boolean;
  error: string | null;
};

type useLogin = {
  loginForm: UseLoginFormReturn;
  showLoginModal: boolean;
  setShowLoginModal: React.Dispatch<React.SetStateAction<boolean>>;
};

const useLoginForm = (
  action: (prevState: LoginState, formData: FormData) => Promise<LoginState>,
  onSuccess: () => void,
  onError: () => void
): UseLoginFormReturn => {
  const [state, formAction, isPending] = useActionState<LoginState, FormData>(
    action,
    {
      success: false,
      error: null,
    }
  );
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);

  useEffect(() => {
    if (state?.success) {
      setIsAuthenticated(true);
      setError(null);
      onSuccess();
    } else {
      setIsAuthenticated(false);
      if (state?.error) {
        setError(state.error);
        onError();
      }
    }
  }, [state?.success, state?.error, onSuccess, onError]);

  return {
    isAuthenticated,
    formAction,
    isPending,
    error,
  };
};

const LoginContext = createContext<useLogin | null>(null);

export const LoginProvider: React.FC<React.PropsWithChildren<{}>> = ({
  children,
}) => {
  const [showLoginModal, setShowLoginModal] = React.useState(false);

  const loginForm = useLoginForm(
    async (prevState, formData) => {
      return submitAction(prevState, formData);
    },
    () => setShowLoginModal(false),
    () => {
      console.log("Login failed");
    }
  );

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
