%pivLU: realiza el pivoteo parcial (por filas) sobre la matriz A del
%sistema Ax=b para la factorización LU

function [A, P]=pivLU(A,P,n,k)
    mayor=abs(A(k,k));
    maxrow=k;
    for s=k+1:n
        if abs(A(s,k))>mayor
            mayor=abs(A(s,k));
            maxrow=s;
        end
    end
    if mayor==0
       fprintf('El sistema no tiene solución única')
    elseif maxrow~=k %intercambio de filas
        aux=A(k,:);
        auxP=P(k,:);
        A(k,:)=A(maxrow,:);
        P(k,:)=P(maxrow,:);
        A(maxrow,:)=aux;
        P(maxrow,:)=auxP;
    end
    
end