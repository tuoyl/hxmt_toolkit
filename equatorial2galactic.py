#!/usr/bin/env python
#
# author: Ge Mingye(gemy@ihep.ac.cn)
#
# convert right ascension and declination in equatorial coordinates
# to galactic coordinates
#
# Ra: in degrees
# Dec: in degrees
# Output: in rad
import numpy

def equatorial2galactic( RA, Dec):

    RA = RA * numpy.pi / 180
    Dec = Dec* numpy.pi / 180
       
    RAgp = 192.85948 * numpy.pi / 180.0
    Decgp = 27.12825 * numpy.pi / 180.0
    lcp = 122.932 * numpy.pi / 180.0
   
    sinb = numpy.sin( Dec ) * numpy.sin( Decgp ) + numpy.cos( Dec ) * numpy.cos( Decgp ) * numpy.cos( RA - RAgp )
    cosbsinlcp_l = numpy.cos( Dec ) * numpy.sin( RA - RAgp )
    cosbcoslcp_l = numpy.sin( Dec ) * numpy.cos( Decgp ) - numpy.cos( Dec ) * numpy.sin( Decgp ) * numpy.cos( RA - RAgp )
   
    b = numpy.arcsin( sinb )
    sinlcp_l = cosbsinlcp_l / numpy.cos( b )
    coslcp_l = cosbcoslcp_l / numpy.cos( b )
   
    if ( sinlcp_l > 0 ) : lcp_l = numpy.arccos( coslcp_l )
    else :
        if ( coslcp_l < 0 ) : lcp_l = 2 * numpy.pi - numpy.arccos( coslcp_l )
        else : lcp_l = numpy.arcsin( sinlcp_l )
    l = lcp - lcp_l
    if ( l < 0 ) : l = 2 * numpy.pi + l
    return [ l, b ]
   
RA = input('RA(degrees): ')
Dec = input('DEC(degrees): ')
lb = equatorial2galactic( 83.6332, 22.0 )
lb = equatorial2galactic( 262.25, -29.0 )
lb = equatorial2galactic( RA, Dec )
print(lb[0]*180/numpy.pi,lb[1]*180/numpy.pi)
