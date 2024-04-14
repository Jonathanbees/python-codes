%pivpar: realiza el pivoteo parcial (por filas) sobre la matriz aumentada AB del
%sistema Ax=b

function Ab = pivpar(Ab,n,k)
    mayor=abs(Ab(k,k));
    maxrow=k;
    for s=k+1:n
        if abs(Ab(s,k))>mayor
            mayor=abs(Ab(s,k));
            maxrow=s;
        end
    end
    if mayor==0
       fprintf('El sistema no tiene solución única')
    elseif maxrow~=k %intercambio de filas
        aux=Ab(k,:);
        Ab(k,:)=Ab(maxrow,:);
        Ab(maxrow,:)=aux;
    end
    
end