FROM render/extras
RUN wget http://ftp.gnu.org/gnu/gcc/gcc-9.3.0/gcc-9.3.0.tar.gz && \
    tar xvfz gcc-9.3.0.tar.gz && \
    cd gcc-9.3.0 && \
    ./configure && \
    make && \
    make install
