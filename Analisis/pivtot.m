%pivtot: realiza el pivoteo total(por filas y columnas) sobre la matriz aumentada AB del
%sistema Ax=b

function [Ab, mark]=pivtot(Ab,mark,n,k)
    mayor=0;
    maxrow=k;
    maxcol=k;
    for r=k:n
        for s=k:n
            if abs(Ab(r,s))>mayor
                mayor=abs(Ab(r,s));
                maxrow=r;
                maxcol=s;
            end
        end
    end
    if mayor==0
        fprintf('El sistema no tiene solución única')
    else
        if maxrow~=k %intercambio de filas
            aux=Ab(k,:);
            Ab(k,:)=Ab(maxrow,:);
            Ab(maxrow,:)=aux;
        end
        if maxcol~=k %intercambio de columnas
            aux=Ab(:,k);
            Ab(:,k)=Ab(:,maxcol);
            Ab(:,maxcol)=aux;
            aux2=mark(k);
            mark(k)=mark(maxcol);
            mark(maxcol)=aux2;
            
        end
    end
    
end