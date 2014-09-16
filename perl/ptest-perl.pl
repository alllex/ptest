#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-11

use strict;
use perl::tests::test;
use perl::tests::addition;

# -------------------------------------------------------
#                     Benchmark utils
# -------------------------------------------------------

sub benchmark {
    use Benchmark;
    use List::Util qw( min );
    my ($name, $test, $rep, $num) = @_;
    my @params = get_data($name);

    my @timed = ();

    for my $param (@params) {
        my @results = ();
        for (1..$rep) { 
            my $bm = timeit($num, sub { $test->(@$param); }); 
            push @results, $bm->cpu_a;
        }
        my $best = min(@results);
        push @timed, [$best, $param];
    }

    return ( # Full benchmark info
        $name,
        $rep,
        $num,
        @timed
    );
}

sub now {
    return "" . localtime();
     # use POSIX qw(strftime);
     # my $t = localtime(); strftime "%a %b %e %H:%M:%S %Y", localtime();
     # return $t;
}

sub mk_logname ($) {
    my $test_name = $_[0];
    my $folder = 'results';
    my $lang = perl::tests::test::subject();
    my $ext = 'log';
    return "$folder/$test_name-$lang.$ext";
}

sub tool_name {
    return 'Perl: ' . (split /\n/, `perl -v`)[1];
}

sub log_benchmark ($) {
    my $bench_args = $_[0];

    my ($test_case, $rep, $num, @timed) = benchmark(@$bench_args);

    my $logname = mk_logname($test_case);

    my $c = $#timed + 1;
    my $a = sprintf "___", 'NONE';

    my $title = "Test case( $test_case ): repeat( $rep ) of number( $num )\nAll $c tests took about $a to process\n";

    open(my $log, '>', $logname);
    print $log tool_name(), "\n";
    print $log $title;
    print $title;

    for (@timed) { 
        my ($time, $params) = @$_;
        $time = sprintf "%8.5f", $time;
        my $to_log = "$time // (" . join(", ", @$params) . ")\n";
        print $log $to_log;
        print $to_log;
    }

    close $log;
}

# -------------------------------------------------------
#                   Test compilation
# -------------------------------------------------------

sub tests {

    # makes test bunch from test name
    sub mk_bunch { # args(module, test case, repeat, number)
        no strict 'refs';
        my $tests_info = shift;
        my $mod = $tests_info->[0];
        my $test = \&{"perl\:\:tests\:\:$mod\:\:test"};
        my $rep = shift;
        my $num = shift;
        my @bunches = ();
        for (@{$tests_info->[1]}) { push @bunches, [ $_, $test, $rep, $num] }
        @bunches;
    }

    my @prefs = get_prefs();
    my $repeat_fast = $prefs[0];
    my $repeat_mid  = $prefs[1];
    my $repeat_slow = $prefs[2];
    my $number_fast = $prefs[3];
    my $number_mid  = $prefs[4];
    my $number_slow = $prefs[5];

    my @fast = (
        ["addition", [
                "AdditionOfInt", 
                "AdditionOfLong", 
                "AdditionOfBigInt"
            ]
        ]
    );

    my @tests = ();
    for (@fast) { push @tests, mk_bunch($_, $repeat_fast, $number_fast); }

    @tests;
}

# -------------------------------------------------------
#                     Test runner
# -------------------------------------------------------

sub main {
    for (tests()) { log_benchmark($_) }
}

main();