import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { Thermometer, Zap, Clock, Power, ShieldCheck, AlertTriangle, Loader2, CheckCircle2, XCircle, Radio } from 'lucide-react';

// ─────────────────────────────────────────────────────────────────────────────
// CONFIG — change MACHINE_ID to match your ESP32's machine_id field
// ─────────────────────────────────────────────────────────────────────────────
const API_BASE = 'http://localhost:8000';
const MACHINE_ID = 'ESP32_Pasteurizer_01';
const POLL_INTERVAL_MS = 2000; // 2 seconds

// ─────────────────────────────────────────────────────────────────────────────
// STATUS BADGE for active command
// ─────────────────────────────────────────────────────────────────────────────
function CommandStatusBadge({ activeCommand }) {
  if (!activeCommand) return null;

  const statusStyles = {
    PENDING:  'bg-yellow-900/40 text-yellow-400 border-yellow-500/50',
    SENT:     'bg-blue-900/40  text-blue-400   border-blue-500/50',
    EXECUTED: 'bg-green-900/40 text-green-400  border-green-500/50',
    REJECTED: 'bg-red-900/40   text-red-400    border-red-500/50',
    FAILED:   'bg-red-900/40   text-red-400    border-red-500/50',
  };
  const statusIcons = {
    PENDING:  <Radio className="w-4 h-4 animate-pulse" />,
    SENT:     <Radio className="w-4 h-4 animate-pulse" />,
    EXECUTED: <CheckCircle2 className="w-4 h-4" />,
    REJECTED: <XCircle className="w-4 h-4" />,
    FAILED:   <XCircle className="w-4 h-4" />,
  };
  const style = statusStyles[activeCommand.status] || statusStyles.PENDING;
  const icon  = statusIcons[activeCommand.status]  || statusIcons.PENDING;

  return (
    <div className={`mt-4 flex items-center justify-between bg-slate-900 p-3 rounded border ${style} text-sm`}>
      <span className="text-slate-400">
        Last Command: <span className="text-white font-bold">{activeCommand.command}</span>
        <span className="text-slate-500 font-mono text-xs ml-2">({activeCommand.command_id})</span>
      </span>
      <span className={`flex items-center gap-1 font-bold uppercase tracking-widest ${style.split(' ')[1]}`}>
        {icon} {activeCommand.status}
      </span>
    </div>
  );
}

// ─────────────────────────────────────────────────────────────────────────────
// MAIN COMPONENT
// ─────────────────────────────────────────────────────────────────────────────
export default function LiveDashboard() {
  const [sensorData, setSensorData]   = useState(null);
  const [error, setError]             = useState(false);
  const [isSending, setIsSending]     = useState(false); // Prevents double-click

  // Track the ID of the last command WE sent so we can highlight its status
  const lastSentCommandIdRef = useRef(null);

  // ── 1. HTTP Polling for live data ─────────────────────────────────────────
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`${API_BASE}/device/live`);
        setSensorData(response.data);
        setError(false);

        // Auto-clear isSending once the command is in a terminal state
        const ac = response.data?.active_command;
        if (
          ac &&
          ac.command_id === lastSentCommandIdRef.current &&
          ['EXECUTED', 'REJECTED', 'FAILED'].includes(ac.status)
        ) {
          setIsSending(false);
        }
      } catch (err) {
        console.error('Error fetching live data:', err);
        setError(true);
      }
    };
    fetchData();
    const interval = setInterval(fetchData, POLL_INTERVAL_MS);
    return () => clearInterval(interval);
  }, []);

  // ── 2. Send a command to the backend ──────────────────────────────────────
  const triggerCommand = async (commandName, parameters = {}) => {
    if (isSending) return;
    setIsSending(true);
    lastSentCommandIdRef.current = null;

    try {
      const response = await axios.post(
        `${API_BASE}/device/${MACHINE_ID}/commands`,
        { command: commandName, parameters }
      );
      lastSentCommandIdRef.current = response.data.command_id;
      console.log(`✅ Command queued: ${response.data.command_id} (${commandName}) — status: ${response.data.status}`);
      // isSending will be cleared when the polling loop sees EXECUTED/REJECTED/FAILED
    } catch (err) {
      console.error('Failed to send command:', err);
      setIsSending(false);
    }
  };

  // ── Helpers ───────────────────────────────────────────────────────────────
  const formatTime = (seconds) => {
    if (seconds === undefined || seconds === null) return '00:00';
    const m = Math.floor(seconds / 60).toString().padStart(2, '0');
    const s = (seconds % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  // ── Loading / Error states ────────────────────────────────────────────────
  if (error) return (
    <div className="p-8 text-xl font-bold text-red-500 flex items-center justify-center h-full bg-slate-900">
      ⚠️ Cannot connect to backend at <code className="ml-2 text-red-400">{API_BASE}</code>.
      <br />Make sure <code>uvicorn main:app</code> is running.
    </div>
  );
  if (!sensorData || Object.keys(sensorData).length === 0) {
    return (
      <div className="flex items-center justify-center h-screen bg-slate-900 text-slate-300">
        <div className="text-center">
          <Loader2 className="w-12 h-12 animate-spin mx-auto mb-4 text-blue-500" />
          <h2 className="text-2xl font-bold">🔌 SCADA System Initializing</h2>
          <p className="mt-2 text-slate-400">Waiting for telemetry from <span className="font-mono text-blue-400">{MACHINE_ID}</span>…</p>
          <p className="mt-1 text-xs text-slate-600">Backend: {API_BASE}</p>
        </div>
      </div>
    );
  }

  const isOnline = sensorData.online;
  const isHolding = sensorData.process_state === 'HOLDING';
  const pipelineStates = ['START', 'HEATING', 'HOLDING', 'COOLING', 'COMPLETE'];
  const activeCommand = sensorData.active_command;

  return (
    <div className="min-h-screen bg-slate-900 p-6 font-sans text-slate-200">
      <div className="max-w-7xl mx-auto flex flex-col gap-6">

        {/* ── Top Bar ── */}
        <div className="flex justify-between items-center bg-slate-800 p-6 rounded-lg border-2 border-slate-700 shadow-lg">
          <div className="flex items-center gap-4">
            <h1 className="text-3xl font-black text-slate-100 tracking-wider">MILK PASTEURIZATION SCADA</h1>
            <span className="bg-slate-900 px-3 py-1 rounded text-sm text-blue-400 font-mono tracking-wider border border-slate-700">
              {sensorData.machine_id}
            </span>
          </div>
          <div className="flex items-center gap-3">
            <span className="font-bold text-slate-400 uppercase text-sm tracking-widest">Status</span>
            <div className={`flex items-center gap-2 px-4 py-2 rounded-full font-bold ${isOnline ? 'bg-green-900/40 text-green-400 border border-green-500/50' : 'bg-red-900/40 text-red-400 border border-red-500/50'}`}>
              <div className={`w-3 h-3 rounded-full ${isOnline ? 'bg-green-500 animate-pulse' : 'bg-red-500'}`}></div>
              {isOnline ? 'ONLINE' : 'OFFLINE'}
            </div>
          </div>
        </div>

        {/* ── Mode & Pipeline ── */}
        <div className="bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg flex flex-col gap-6">
          <div className="flex justify-between items-center">
            <div className="flex gap-4">
              <div className="bg-slate-900 p-4 rounded border border-slate-700 min-w-[150px]">
                <div className="text-slate-500 text-xs font-bold uppercase tracking-wider mb-1">Control Mode</div>
                <div className="text-xl font-bold text-blue-400">{sensorData.mode || 'UNKNOWN'}</div>
              </div>
              <div className="bg-slate-900 p-4 rounded border border-slate-700 min-w-[150px]">
                <div className="text-slate-500 text-xs font-bold uppercase tracking-wider mb-1">Process State</div>
                <div className="text-xl font-bold text-emerald-400">{sensorData.process_state || 'IDLE'}</div>
              </div>
            </div>
          </div>

          <div className="flex items-center w-full bg-slate-900 p-4 rounded border border-slate-700 overflow-x-auto">
            {pipelineStates.map((state, index) => {
              const isActive = sensorData.process_state === state;
              const isPast = pipelineStates.indexOf(sensorData.process_state) > index;
              return (
                <div key={state} className="flex-1 flex items-center min-w-[120px]">
                  <div className={`flex-1 text-center py-2 rounded font-bold text-sm tracking-wider whitespace-nowrap
                    ${isActive ? 'bg-blue-600 text-white shadow-[0_0_15px_rgba(37,99,235,0.5)]' :
                      isPast ? 'text-slate-400' : 'text-slate-600'}`}>
                    [ {state} ]
                  </div>
                  {index < pipelineStates.length - 1 && (
                    <div className="w-8 flex justify-center">
                      <span className={isPast ? 'text-blue-500' : 'text-slate-700'}>→</span>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>

        {/* ── Main Dashboard Grid ── */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

          {/* Column 1: Temperature & Timers */}
          <div className="lg:col-span-1 flex flex-col gap-6">
            <div className="bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg relative overflow-hidden h-full flex flex-col justify-center text-center group">
              <Thermometer className="absolute -top-4 -left-4 w-32 h-32 text-slate-700/30 group-hover:text-blue-500/10 transition-colors" />
              <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-2 z-10">Temperature</h3>
              <div className="text-7xl font-black text-white z-10">
                {(sensorData.temperature || 0).toFixed(1)}<span className="text-3xl text-slate-500">°C</span>
              </div>

              <div className="grid grid-cols-2 gap-4 mt-8 z-10">
                <div className="bg-slate-900 p-3 rounded border border-slate-700">
                  <div className="text-xs text-slate-500 uppercase font-bold">Target</div>
                  <div className="text-lg font-bold text-blue-400">{sensorData.target_temperature || 0}°C</div>
                </div>
                <div className="bg-slate-900 p-3 rounded border border-slate-700">
                  <div className="text-xs text-slate-500 uppercase font-bold">Diff</div>
                  <div className="text-lg font-bold text-amber-400">
                    {Math.abs((sensorData.temperature || 0) - (sensorData.target_temperature || 0)).toFixed(1)}°C
                  </div>
                </div>
              </div>
            </div>

            {/* Conditional Holding Timer */}
            {isHolding && (
              <div className="bg-slate-800 p-6 rounded-lg border-2 border-emerald-500/50 shadow-[0_0_20px_rgba(16,185,129,0.1)] text-center animate-pulse">
                <Clock className="w-8 h-8 text-emerald-500 mx-auto mb-2" />
                <h3 className="text-slate-300 font-bold uppercase tracking-widest mb-2">Holding Timer</h3>
                <div className="flex justify-center items-center gap-4 text-3xl font-mono font-bold text-emerald-400">
                  <span>{formatTime(sensorData.holding_elapsed_sec)}</span>
                  <span className="text-slate-600">/</span>
                  <span>{formatTime(sensorData.holding_time_sec)}</span>
                </div>
                <div className="mt-2 text-sm text-emerald-600 font-bold">
                  REMAINING: {formatTime(sensorData.holding_remaining_sec)}
                </div>
              </div>
            )}
          </div>

          {/* Column 2: Equipment Relays */}
          <div className="lg:col-span-2 flex flex-col gap-6">
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
              {[
                { name: 'HEATER',  state: sensorData.heater  },
                { name: 'STIRRER', state: sensorData.stirrer },
                { name: 'COOLER',  state: sensorData.cooler  }
              ].map(equip => (
                <div key={equip.name} className={`bg-slate-800 p-6 rounded-lg border ${equip.state ? 'border-green-500/50' : 'border-slate-700'} shadow-lg flex flex-col items-center justify-center transition-all`}>
                  <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-4">{equip.name}</h3>
                  <div className={`w-16 h-16 rounded-full flex items-center justify-center mb-4 transition-colors ${equip.state ? 'bg-green-500 shadow-[0_0_20px_rgba(34,197,94,0.4)]' : 'bg-slate-700'}`}>
                    <Power className={`w-8 h-8 ${equip.state ? 'text-white' : 'text-slate-900'}`} />
                  </div>
                  <div className={`text-2xl font-black ${equip.state ? 'text-green-400' : 'text-slate-600'}`}>
                    {equip.state ? 'ON' : 'OFF'}
                  </div>
                </div>
              ))}
            </div>

            {/* Electrical Telemetry */}
            <div className="bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg">
              <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-4 flex items-center gap-2">
                <Zap className="w-5 h-5 text-yellow-500" />
                Electrical Telemetry
              </h3>
              <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
                {[
                  { label: 'VOLTAGE', val: (sensorData.voltage      || 0).toFixed(1),  unit: 'V'   },
                  { label: 'CURRENT', val: (sensorData.current      || 0).toFixed(2),  unit: 'A'   },
                  { label: 'POWER',   val: (sensorData.power        || 0).toFixed(1),  unit: 'W'   },
                  { label: 'ENERGY',  val: (sensorData.energy       || 0).toFixed(3),  unit: 'kWh' },
                  { label: 'FREQ',    val: (sensorData.frequency    || 0).toFixed(1),  unit: 'Hz'  },
                  { label: 'PF',      val: (sensorData.power_factor || 0).toFixed(2),  unit: ''    }
                ].map(metric => (
                  <div key={metric.label} className="bg-slate-900 p-3 rounded border border-slate-800 text-center">
                    <div className="text-[10px] text-slate-500 font-bold uppercase tracking-widest mb-1">{metric.label}</div>
                    <div className="text-lg font-mono font-bold text-slate-200">
                      {metric.val} <span className="text-xs text-slate-500">{metric.unit}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* ── Bottom: Control Panel & Alarms ── */}
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          <div className="lg:col-span-3 bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg">
            <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-4 flex items-center gap-2">
              <ShieldCheck className="w-5 h-5 text-blue-500" />
              Command Center
            </h3>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
              <button
                id="btn-auto-start"
                onClick={() => triggerCommand('AUTO_START', { target_temperature: 72.0, hold_time: 15, cool_temperature: 35.0 })}
                disabled={isSending}
                className="w-full bg-green-700 hover:bg-green-600 disabled:bg-slate-700 disabled:cursor-not-allowed text-white py-4 rounded font-bold uppercase tracking-wider transition-colors"
              >
                Auto Start
              </button>
              <button
                id="btn-manual"
                onClick={() => triggerCommand('MANUAL_MODE')}
                disabled={isSending}
                className="w-full bg-blue-700 hover:bg-blue-600 disabled:bg-slate-700 disabled:cursor-not-allowed text-white py-4 rounded font-bold uppercase tracking-wider transition-colors"
              >
                Manual
              </button>
              <button
                id="btn-stop"
                onClick={() => triggerCommand('STOP')}
                disabled={isSending}
                className="w-full bg-amber-700 hover:bg-amber-600 disabled:bg-slate-700 disabled:cursor-not-allowed text-white py-4 rounded font-bold uppercase tracking-wider transition-colors"
              >
                Stop
              </button>
              <button
                id="btn-emergency-stop"
                onClick={() => triggerCommand('EMERGENCY_STOP')}
                disabled={isSending}
                className="w-full bg-red-700 hover:bg-red-600 disabled:bg-slate-700 disabled:cursor-not-allowed text-white py-4 rounded font-bold uppercase tracking-wider transition-colors flex items-center justify-center gap-2"
              >
                <AlertTriangle className="w-5 h-5" /> E-STOP
              </button>
            </div>

            {/* Live Command Status (driven by backend state) */}
            <CommandStatusBadge activeCommand={activeCommand} />
          </div>

          {/* Fault / Alarm Panel */}
          <div className="lg:col-span-1 bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg">
            <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-4 flex items-center gap-2">
              <AlertTriangle className={`w-5 h-5 ${sensorData.fault ? 'text-red-500 animate-pulse' : 'text-slate-500'}`} />
              Active Alarms
            </h3>
            <div className={`h-full min-h-[80px] rounded flex items-center justify-center border p-4 ${sensorData.fault ? 'bg-red-900/30 border-red-500 text-red-500' : 'bg-slate-900 border-slate-700 text-slate-500'}`}>
              {sensorData.fault ? (
                <div className="text-center font-bold">
                  <div className="text-xl uppercase">FAULT DETECTED</div>
                  <div className="text-sm font-mono mt-1">{sensorData.fault_code || 'UNKNOWN ERROR'}</div>
                </div>
              ) : (
                <div className="font-bold uppercase tracking-wider text-sm text-center">No active alarms</div>
              )}
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}
