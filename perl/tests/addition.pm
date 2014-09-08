#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-07

# -------------------------------------------------------
#                     Addition Tests
# -------------------------------------------------------

package perl::tests::addition;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test &params);
@EXPORT_OK   = qw(test params);
# %EXPORT_TAGS = ( DEFAULT => [qw(&func1)],
#                  Both    => [qw(&func1 &func2)]);

sub test ($$)  { return $_[0] + $_[1] }
sub params {
    open (my $file, "<", "data/gen/AdditionOfInt.data") || die "Can't read file: $!";
    my @lines = <$file>;
    # TODO split arguments into chunks
    # print @lines;
    close($file);
}

1;