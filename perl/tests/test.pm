#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-11

# -------------------------------------------------------
#                     Addition Tests
# -------------------------------------------------------

package perl::tests::test;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&get_data);
@EXPORT_OK   = qw(get_data);

sub get_data ($) {
    my $test_name = $_[0];
    my $file_name = "data/gen/$test_name.data";
    open (my $file, "<", $file_name) || die "Can't read file: $!";
    map[ split ], <$file>;
}

1;