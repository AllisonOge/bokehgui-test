#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BokehGUI test
# Author: Allison Ogechukwu
# GNU Radio version: 3.10.3.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import bokehgui




class test_bokehgui(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "BokehGUI test", catch_exceptions=True)
        self.plot_lst = []
        self.widget_lst = []

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.bokehgui_waterfall_sink_x_0 = bokehgui.waterfall_sink_c_proc(1024, window.WIN_BLACKMAN_hARRIS, 0,samp_rate, "")

        legend_list = []
        for i in  range(1):
          if len('') == 0:
            legend_list.append("Data {0}".format(i))
          else:
            legend_list.append('')
        self.bokehgui_waterfall_sink_x_0_plot = bokehgui.waterfall_sink_c(self.plot_lst, self.bokehgui_waterfall_sink_x_0, update_time = 100,
                      legend_list = legend_list, palette = 'Inferno',
                      values_range = [-140, 10], is_message =    False  )

        self.bokehgui_waterfall_sink_x_0_plot.set_y_label('Time' + '(' +''+')')
        self.bokehgui_waterfall_sink_x_0_plot.set_x_label('Frequency' + '(' +'Hz'+')')
        self.bokehgui_waterfall_sink_x_0_plot.enable_grid(False)
        self.bokehgui_waterfall_sink_x_0_plot.enable_legend(True)
        self.bokehgui_waterfall_sink_x_0_plot.set_layout(*((0,1)))
        self.bokehgui_time_sink_x_0 = bokehgui.time_sink_c_proc(1024, samp_rate, "",
         1
        )


        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        legend_list = []
        for i in  range(       2*1    ):
          if len(labels[i]) == 0:
            if(i % 2 == 0):
              legend_list.append("Re{{Data {0}}}".format(i/2))
            else:
              legend_list.append("Im{{Data {0}}}".format(i/2))
          else:
            legend_list.append(labels[i])

        self.bokehgui_time_sink_x_0_plot = bokehgui.time_sink_c(self.plot_lst, self.bokehgui_time_sink_x_0, log_x = False, log_y = False, update_time = 100, legend_list = legend_list, is_message =   False)

        self.bokehgui_time_sink_x_0_plot.set_y_axis([-1, 1])
        self.bokehgui_time_sink_x_0_plot.set_y_label('Amplitude' + '(' +""+')')
        self.bokehgui_time_sink_x_0_plot.set_x_label('Time' + '(' +""+')')

        self.bokehgui_time_sink_x_0_plot.enable_tags(-1, True)
        self.bokehgui_time_sink_x_0_plot.set_trigger_mode(bokehgui.TRIG_MODE_FREE, bokehgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.bokehgui_time_sink_x_0_plot.enable_grid(False)
        self.bokehgui_time_sink_x_0_plot.enable_axis_labels(True)
        self.bokehgui_time_sink_x_0_plot.enable_legend(True)
        self.bokehgui_time_sink_x_0_plot.set_layout(*((1,1)))

        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "blue", "blue", "blue"]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        styles = ["solid", "solid", "solid", "solid", "solid",
                  "solid", "solid", "solid", "solid", "solid"]
        markers = [None, None, None, None, None,
                  None, None, None, None, None]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in  range(  2*1  ):
            self.bokehgui_time_sink_x_0_plot.format_line(i, colors[i], widths[i], styles[i], markers[i], alphas[i])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.bokehgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.bokehgui_waterfall_sink_x_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.bokehgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.bokehgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)




def main(top_block_cls=test_bokehgui, options=None):
    # Create Top Block instance
    tb = top_block_cls()

    try:
        tb.start()

        bokehgui.utils.run_server(tb, sizing_mode = "fixed",  widget_placement =  (0, 0), window_size =  (1000, 1000))
    finally:
        print("Exiting the simulation. Stopping Bokeh Server")
        tb.stop()
        tb.wait()


if __name__ == '__main__':
    main()
