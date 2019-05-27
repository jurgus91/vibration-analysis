%load ABS_z1_pomiar_1
Fs=VCAP_SAMPLERATE;
A=VCAP_DATA;
n=length(A);
k=1/Fs;
t=0:k:(n-1)*k;
x=A(:,1);
y=A(:,2);
z=A(:,3);
zn=A(:,4);
figure(9)
plot(t,x)
figure(10)
plot(t,y)
figure(11)
plot(t,z)
figure(12)
plot(t,zn)
X=abs(fft(x))/(n/2);
X=X(1:n/2);
Y=abs(fft(y))/(n/2);
Y=Y(1:n/2);
Z=abs(fft(z))/(n/2);
Z=Z(1:n/2);
ZN=abs(fft(zn))/(n/2);
ZN=ZN(1:n/2);
f=Fs*(0:n/2-1)/n;

figure(13)
subplot(311)
plot(f,X)
subplot(312)
plot(f,Y)
subplot(313)
plot(f,Z)
figure(14)
plot(f,ZN)


%obliczenie wartości skutecznej dla przemieszczeń





