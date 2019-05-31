%SundarLabProgram
%fft analysis for x,y,z values from accelerometer
function Y= fftDataAnalysis(filename) 
       %format long;
       fid=fopen(filename);
       if fid < 0 % zero is returned if file does not exist
         % display an error message and halt execution of the program
         error('File Does Not Exist');
       end

       A=textscan(fid,'%f%f%f%f','Delimiter',':,,\n');
       A=makeArraySameSize(A);
       A{2};
       analysis(A);
       %t=[A{1},A{2},A{3},A{4}]
       avgX=mean(A{2});
       avgY=mean(A{3});
       avgZ=mean(A{4});
             
        fs = 1000; % Sample Frequency [Hz]
        ts = 20; %time per sample period
        num_split = ts*fs; % number of data points per sample period
        num_samples = floor(length(A)/num_split);
        
        
        for m = 0:num_samples-1
            A = A(m*num_split+1:num_split*(m+1),:); % First column of Cell is raw acclerometer data
            A = fft(A); % generates the fft transformation of raw accelerometer data
        end
       %disp(A{2})
       subplot(3,1,1)
       plot(A{2})
       subplot(3,1,2)
       plot(A{3})
       subplot(3,1,3)
       plot(A{4})

       
       fprintf("Average X Reading: %.3f\n",avgX)
       fprintf("Average Y Reading: %.3f\n",avgY)
       fprintf("Average Z Reading: %.3f\n",avgZ)
        
       
       
end

function [A]=makeArraySameSize(A)
    maxLength=length(A{1});
    incompleteTest=0;
    
    for i=2:length(A)
        lengthTemp=length(A{i});
        if(lengthTemp<maxLength)
            maxLength=lengthTemp;
            incompleteTest=1;
        end

         
    end
   
    if(incompleteTest==1)
        for i=1:length(A)
            if(length(A{i})~=maxLength)
               %fprintf("entered")
                %length(A{i});
                A{i}(maxLength+1,:)=[];
            
            end
        end
    end
    
end