#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-11

use strict;
use perl::tests::test;

BEGIN {
    require perl::tests::arithmetic;
    import addition;
    import multiplication;

    require perl::tests::loops;
    import loop_for_c;
    import loop_for_range;
    import loop_while;
    import loop_foreach;

    require perl::tests::factorials;
    import fact_by_mathlib;
    import fact_by_rec;
    import fact_by_loop;

    require perl::tests::gcds;
    import gcd_by_rec;
    import gcd_by_loop;
}

# -------------------------------------------------------
#                     Benchmark utils
# -------------------------------------------------------

sub benchmark {
    use Benchmark;
    use List::Util qw( min );
    my ($name, $test, $data_key, $rep, $num) = @_;
    my @params = get_data($data_key);

    my @timed = ();

    for my $param (@params) {
        my @results = ();
        for (1..$rep) { 
            my $bm = timeit($num, sub { $test->(@$param); }); 
            push @results, $bm->cpu_a;
        }
        my $best = min(@results);
        my $res  = $test->(@$param);
        push @timed, [$best, $param, $res];
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
    my $start_time = time;
    my ($test_case, $rep, $num, @timed) = benchmark(@$bench_args);
    my $diff = time - $start_time;
    my $logname = mk_logname($test_case);

    my $c = sprintf "%2d", $#timed + 1;
    my $a = sprintf "%3ds", $diff;

    my $title = "Test case( $test_case ): repeat( $rep ) of number( $num )\nAll $c tests took about $a to process\n";

    open(my $log, '>', $logname);
    print $log tool_name(), "\n";
    print $log $title;
    print $title;

    for (@timed) { 
        my ($time, $param, $res) = @$_;
        $time = sprintf "%8.5f", $time;
        my $to_log = "$time // f(" . join(", ", @$param) . ") = $res\n";
        print $log $to_log;
        # print $to_log;
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
        my $test = \&{"perl\:\:tests\:\:$mod\:\:test_$mod"};
        my $data_key = $tests_info->[1];
        my $rep = shift;
        my $num = shift;
        my @bunches = ();
        for (@{$tests_info->[2]}) { push @bunches, [ $_, $test, ($data_key eq "") ? $_ : $data_key, $rep, $num] }
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

        ["addition", "", [
                "AdditionOfInt", 
                "AdditionOfLong"
            ]
        ],

        ["multiplication", "", [
                "MultiplicationOfInt", 
                "MultiplicationOfLong"
            ]
        ]
    );

    my @mid = (

        ["loop_for_c", "Loop", [ "LoopForC" ]],
        ["loop_for_range", "Loop", [ "LoopForRange" ]],
        ["loop_while", "Loop", [ "LoopWhile" ]],
        ["loop_foreach", "Loop", [ "LoopForeach" ]],

        ["fact_by_mathlib", "Factorial", [ "FactorialByMathLib" ]],
        ["fact_by_rec", "Factorial", [ "FactorialByRec" ]],
        ["fact_by_loop", "Factorial", [ "FactorialByLoop" ]],

        ["gcd_by_rec", "GCD", [ "GCDByRec" ]],
        ["gcd_by_loop", "GCD", [ "GCDByLoop" ]],
    );

    my @slow = (
    );



    my @tests = ();
    for (@fast) { push @tests, mk_bunch($_, $repeat_fast, $number_fast); }
    for (@mid)  { push @tests, mk_bunch($_, $repeat_mid, $number_mid); }
    for (@slow)  { push @tests, mk_bunch($_, $repeat_slow, $number_slow); }

    @tests;
}

# -------------------------------------------------------
#                     Test runner
# -------------------------------------------------------

sub main {
    for (tests()) { log_benchmark($_) }
}

main();