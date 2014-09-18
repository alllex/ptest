#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-18

# -------------------------------------------------------
#                     Addition Tests
# -------------------------------------------------------

package perl::tests::addition;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_addition);
@EXPORT_OK   = qw(test_addition);

sub test_addition { $_[0] + $_[1] }

# -------------------------------------------------------
#                  Multiplication Tests
# -------------------------------------------------------

package perl::tests::multiplication;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_multiplication);
@EXPORT_OK   = qw(test_multiplication);

sub test_multiplication { $_[0] * $_[1] }

1;