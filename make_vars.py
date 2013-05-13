#!/usr/bin env python
# -*- coding: utf-8 -*-
"""Make some plots of the velocity widths from the cosmo runs"""

import matplotlib
matplotlib.use('PDF')

import matplotlib.pyplot as plt

import plot_spectra as ps
import vel_data
import os.path as path
import numpy as np
from save_figure import save_figure

base="/home/spb/scratch/Cosmo/"
outdir = base + "plots/vars/"
print "Plots at: ",outdir

def plot_virial_vel(sim, snap, ff=False):
    """Histograms of the velocity width / virial velocity for three different regimes"""
    halo = "Cosmo"+str(sim)+"_V6"
    if ff:
        halo+="_512"
    #Load from a save file only
    hspec = ps.PlotHaloSpectra(snap, base+halo)
    plot_virial_vel_vs_vel_width(self,elem="Si", line=2):
    plt.ylim(0,0.7)

def plot_rel_vel_width_temp(sim1, snap):
    """Load and make a plot of the difference from neglecting temperature broadening"""
    halo1 = "Cosmo"+str(sim1)+"_V6"
    hspec1 = ps.PlottingSpectra(snap, base+halo1, None, None)
    (vbin, vels1) = hspec1.vel_width_hist("Si", 2)
    [rho, vel, temp] = hspec1.metals[("Si", 2)][:3]
    #Compute tau for this metal ion
    (nlos, nbins) = np.shape(rho)
    print sim1,"temp = ",np.mean(temp),np.median(temp)
    tau_tt = np.array([hspec1.compute_absorption("Si", 2, 2, rho[n,:], vel[n,:], np.median(temp)*np.ones_like(temp[n,:])) for n in xrange(0, nlos)])
    (vbin, vels2) = hspec1.vel_width_hist("Si", 2,tau=tau_tt)
    plt.loglog(vbin, vels2, color="blue", lw=3)
    plt.loglog(vbin, vels1, color="red", lw=3)
    vel_data.plot_prochaska_2008_data()
    save_figure(path.join(outdir,"cosmo"+str(ii)+"_no_temp_z"+str(snap)))
    plt.clf()
    mm = np.min((np.size(vels2), np.size(vels1)))
    plt.semilogx(vbin[:mm], vels2[:mm]/vels1[:mm], color="black")
    save_figure(path.join(outdir,"cosmo"+str(ii)+"_no_temp_rel_z"+str(snap)))
    plt.clf()


def plot_rel_vel_width_vel(sim1, snap):
    """Load and make a plot of the difference from neglecting velocity broadening"""
    halo1 = "Cosmo"+str(sim1)+"_V6"
    hspec1 = ps.PlotHaloSpectra(snap, base+halo1, None, None)
    hspec1.plot_vel_width("Si", 2, color="red")
    [rho, vel, temp] = hspec1.metals[("Si", 2)][:3]
    #Compute tau for this metal ion
    (nlos, nbins) = np.shape(rho)
    print sim1,"vel = ",np.mean(vel),np.median(vel)
    #Use virial velocity of halo at this radius
    virial = np.repeat(np.sqrt(4.302e-3*hspec1.sub_mass/1000),3)
    pzpos = np.arange(0,hspec1.nbins)*hspec1.box/hspec1.nbins
    offset = np.sqrt(np.add.outer(hspec1.line_offsets()**2,pzpos**2))
    tau_vv = np.array([hspec1.compute_absorption("Si", 2, 2, rho[n,:], virial[n]/offset[n,:], temp[n,:]) for n in xrange(0, nlos)])
    (vbin, vels2) = hspec1.vel_width_hist("Si", 2,tau=tau_vv)
    plt.loglog(vbin, vels2, color="blue", lw=3)
    vel_data.plot_prochaska_2008_data()
    save_figure(path.join(outdir,"cosmo"+str(ii)+"_no_vel_z"+str(snap)))
    plt.clf()
    (vbin, vels1) = hspec1.vel_width_hist("Si", 2)
    mm = np.min((np.size(vels2), np.size(vels1)))
    plt.semilogx(vbin[:mm], vels2[:mm]/vels1[:mm], color="black")
    save_figure(path.join(outdir,"cosmo"+str(ii)+"_no_vel_rel_z"+str(snap)))
    plt.clf()


#for ii in (0,3):
    ##Plot effect of ignoring temperature broadening
    #plot_rel_vel_width_temp(ii, 60)

#for ii in (0,3):
    ##Plot effect of ignoring temperature broadening
    #plot_rel_vel_width_vel(ii, 60)

for ii in (0,1,2,3):
    #Plot halo mass vs vw.
    plot_virial_vel(ii, 60)
    save_figure(path.join(outdir,"cosmo"+str(ii)+"z3_sub_mass"))
    plt.clf()